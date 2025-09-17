import sys
import os
import re
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QToolBar, QComboBox, QFileDialog, QMessageBox
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWebEngineCore import QWebEngineSettings, QWebEngineProfile
from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QAction
from graph.graphtheory import internal_graph, build_graph_visualization


class HTMLViewerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("HTML Viewer")
        self.setGeometry(100, 100, 1200, 800)
        
        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # Create toolbar
        self.create_toolbar()
        
        # Create web engine view with proper settings
        self.web_view = QWebEngineView()
        self.setup_web_settings()
        layout.addWidget(self.web_view)
        
        # Load a default HTML content
        self.load_default_html()
    
    def setup_web_settings(self):
        """Configure WebEngine settings to allow external resources"""
        # Get the default profile and settings
        profile = QWebEngineProfile.defaultProfile()
        settings = self.web_view.settings()
        
        # Enable all necessary features
        settings.setAttribute(QWebEngineSettings.WebAttribute.JavascriptEnabled, True)
        settings.setAttribute(QWebEngineSettings.WebAttribute.LocalContentCanAccessRemoteUrls, True)
        settings.setAttribute(QWebEngineSettings.WebAttribute.LocalContentCanAccessFileUrls, True)
        settings.setAttribute(QWebEngineSettings.WebAttribute.ErrorPageEnabled, True)
        settings.setAttribute(QWebEngineSettings.WebAttribute.PluginsEnabled, True)
        
        # Allow cross-origin requests
        try:
            # These might not be available in all PyQt6 versions
            settings.setAttribute(QWebEngineSettings.WebAttribute.LocalStorageEnabled, True)
            settings.setAttribute(QWebEngineSettings.WebAttribute.XSSAuditingEnabled, False)
        except:
            pass
        
        # Set user agent to mimic a regular browser
        profile.setHttpUserAgent("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
    
    def create_toolbar(self):
        toolbar = QToolBar()
        self.addToolBar(toolbar)
        
        # Add Open File action
        open_action = QAction("Open HTML", self)
        open_action.triggered.connect(self.open_html_file)
        toolbar.addAction(open_action)
        
        # Add separator
        toolbar.addSeparator()
        
        # Add combobox with placeholder functions
        self.function_combo = QComboBox()
        self.function_combo.addItems([
            "Select Function...",
            "Load Organization Workflow",
            "Reload Page",
            "Clear View"
        ])
        self.function_combo.currentTextChanged.connect(self.on_function_selected)
        toolbar.addWidget(self.function_combo)
    
    def load_default_html(self):
        """Load default HTML content"""
        default_html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>HTML Viewer</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 40px; }
                h1 { color: #333; }
                .content { background: #f5f5f5; padding: 20px; border-radius: 8px; }
                .error { background: #ffe6e6; color: #d00; padding: 15px; border-radius: 5px; margin: 10px 0; }
            </style>
        </head>
        <body>
            <h1>Welcome to HTML Viewer</h1>
            <div class="content">
                <p>This is a minimal PyQt6 application that can display HTML files.</p>
                <p>Use the toolbar to:</p>
                <ul>
                    <li>Open HTML files from your system</li>
                    <li>Select functions from the dropdown menu</li>
                    <li>Fix HTML files with missing dependencies</li>
                </ul>
                <p>You can customize the functions in the combobox to suit your needs.</p>
            </div>
        </body>
        </html>
        """
        self.web_view.setHtml(default_html)
    
    def open_html_file(self):
        """Open and display an HTML file"""
        file_path, _ = QFileDialog.getOpenFileName(
            self, 
            "Open HTML File", 
            "", 
            "HTML Files (*.html *.htm);;All Files (*)"
        )
        
        if file_path:
            if os.path.exists(file_path):
                # Check if it's a pyvis file and needs fixing
                if self.is_pyvis_file(file_path) and self.needs_fixing(file_path):
                    fixed_path = self.auto_fix_pyvis_file(file_path)
                    if fixed_path:
                        file_path = fixed_path
            
                url = QUrl.fromLocalFile(os.path.abspath(file_path))
                self.web_view.load(url)
            else:
                QMessageBox.warning(self, "Error", "File not found!")
    
    def is_pyvis_file(self, file_path):
        """Check if the HTML file is generated by pyvis"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read(2000)  # Read first 2000 chars
                return 'vis-network' in content or 'pyvis' in content.lower()
        except:
            return False
    
    def needs_fixing(self, file_path):
        """Check if the file has the utils.js dependency issue"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                return 'lib/bindings/utils.js' in content
        except:
            return False
    
    def auto_fix_pyvis_file(self, file_path):
        """Automatically fix a pyvis file and return the path to the fixed file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Remove the problematic utils.js reference
            content = content.replace(
                '<script src="lib/bindings/utils.js"></script>', 
                '<!-- utils.js removed - fixed by PyQt6 HTML Viewer -->'
            )
            
            # Add error handling for vis.js loading
            if 'drawGraph();' in content and 'typeof vis === \'undefined\'' not in content:
                content = content.replace(
                    'drawGraph();',
                    '''
                    // Auto-fix: Added error handling for vis.js loading
                    try {
                        if (typeof vis === 'undefined') {
                            console.error('vis.js library not loaded');
                            document.getElementById('mynetwork').innerHTML = 
                                '<div style="padding: 20px; text-align: center; color: red;">' +
                                '<h3>Error: vis.js library failed to load</h3>' +
                                '<p>Please check your internet connection and reload the page.</p>' +
                                '</div>';
                        } else {
                            drawGraph();
                        }
                    } catch (error) {
                        console.error('Error drawing graph:', error);
                        document.getElementById('mynetwork').innerHTML = 
                            '<div style="padding: 20px; text-align: center; color: red;">' +
                            '<h3>Error rendering graph</h3>' +
                            '<p>' + error.message + '</p>' +
                            '</div>';
                    }
                    '''
                )
            
            # Create fixed file path
            base_name = os.path.splitext(file_path)[0]
            fixed_file_path = f"{base_name}_fixed.html"
            
            # Write the fixed content
            with open(fixed_file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            return fixed_file_path
            
        except Exception as e:
            QMessageBox.warning(self, "Auto-fix Error", f"Failed to auto-fix file:\n{str(e)}")
            return None
    
    def on_function_selected(self, text):
        """Handle combobox selection - placeholder functions"""
        if text == "Select Function...":
            return
        elif text == "Load Organization Workflow":
            self.load_internal_org_graph()
        elif text == "Reload Page":
            self.reload_page()
        elif text == "Clear View":
            self.clear_view()
        
        # Reset combobox to default
        self.function_combo.setCurrentIndex(0)

    def load_internal_org_graph(self):
        """Loads internal organization graph"""
        graph = internal_graph()
        html = build_graph_visualization(graph)
        self.web_view.setHtml(html)
    
    def reload_page(self):
        """Reload the current page"""
        self.web_view.reload()
    
    def clear_view(self):
        """Clear the web view"""
        self.web_view.setHtml("")

def main():
    app = QApplication(sys.argv)
    window = HTMLViewerApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()