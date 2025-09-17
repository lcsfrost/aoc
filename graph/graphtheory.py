"""
burrito_graph.py
Example of using NetworkX + PyVis for interactive workflow graphs
with expandable "black box" nodes.
"""
import os
import networkx as nx
from pyvis.network import Network


def internal_graph():
    G = nx.MultiDiGraph()
    
    #Customer Nodes (Simplified)
    G.add_node("Customer Purchasing", group="External")
    G.add_node("Customer Receiving", group="External")

    #Accounting
    G.add_node("Accounts Receivable", group="Accounting")
    G.add_node("Accounts Payable", group="Accounting")
    # G.add_node("Financial Controller", group="Accounting")
    
    #Production
    G.add_node("Plasma", group="Production")
    G.add_node("Forming", group="Production")
    G.add_node("Fabrication", group="Production")

    #Shipping
    G.add_node("Shipping Receiving", group="Shipping")
    G.add_node("Shipping Outgoing", group="Shipping")
    G.add_node("Inventory", group="Shipping")

    #Sales & Project Management
    G.add_node("Sales", group="Sales")

    G.add_edge("Sales", "Plasma", flow="CNC Plasma Order")
    G.add_edge("Sales", "Forming", flow="Forming Work Order")
    G.add_edge("Sales", "Fabrication", flow="Fabrication Work Order")

    G.add_edge("Plasma", "Forming", flow="Flat parts for forming")

    G.add_edge("Plasma", "Shipping Outgoing", flow="Completed flat parts")
    G.add_edge("Forming", "Shipping Outgoing", flow="Formed parts")
    G.add_edge("Fabrication", "Shipping Outgoing", flow="Completed Assemblies")

    G.add_edge("Shipping Receiving", "Inventory", flow="Received Plates")
    G.add_edge("Shipping Receiving", "Accounts Payable", flow="Receiving Records")
    G.add_edge("Inventory", "Plasma", flow="Plates for processing")
    G.add_edge("Inventory", "Shipping Outgoing", flow="Direct plate sales")

    G.add_edge("Shipping Outgoing", "Accounts Receivable", flow="Packing Slip")

    G.add_edge("Customer Purchasing", "Sales", flow="Incoming RFQ")
    G.add_edge("Sales", "Customer Purchasing", flow="Quote Sent")
    G.add_edge("Customer Purchasing", "Sales", flow="Quote Accepted")
    G.add_edge("Shipping Outgoing", "Customer Receiving", flow="Completed Order")

    G.add_edge("Plate Supplier", "Shipping Receiving", flow="Plates Delivered")
    return G




def build_graph_visualization(G, output_file="workflow.html"):
    net = Network(height="1000px", width="100%", directed=True, notebook=False)
    net.toggle_physics(True)
    net.set_options("""
    {
    "physics": {
        "barnesHut": {
        "gravitationalConstant": -2000,
        "centralGravity": 0.05,
        "springLength": 400,
        "springConstant": 0.02
        },
        "stabilization": { "iterations": 2500 }
    },
    "edges": {
        "smooth": { "type": "dynamic" }
    }
    }
    """)
    # Add nodes
    for node, attrs in G.nodes(data=True):
        label = node
        title = f"{node}\nGroup: {attrs.get('group','')}"
        if "parent" in attrs:
            title += f"\nParent: {attrs['parent']}"
        if attrs.get("expandable"):
            # label += " [+]"
            1
        net.add_node(
            node,
            label=label,
            title=title,
            group=attrs.get("group"),
            shape="circle",
            font={"size": 16, "color": "black", "vadjust": 0}
        )

    # Add edges
    for u, v, attrs in G.edges(data=True):
        relation = attrs.get("flow", "")
        net.add_edge(
            u,
            v,
            label=relation,
            title=relation,
            font={"size": 14, "align": "top", "strokeWidth": 3, "strokeColor": "white"},
            smooth=True
        )

    # Write HTML and append click handlers
    # net.generate_html("output.html", local=True, notebook=False)
    net.write_html(output_file, open_browser=False)
    javascript = """
<script type="text/javascript">
  network.on("click", function (params) {
    if (params.nodes.length > 0) {
      var nodeId = params.nodes[0];
    }
  });
</script>
<script type="text/javascript">
  var menu = document.createElement("div");
  menu.id = "nodeMenu";
  menu.style.position = "absolute";
  menu.style.display = "none";
  menu.style.background = "white";
  menu.style.border = "1px solid #ccc";
  menu.style.padding = "5px";
  document.body.appendChild(menu);

  network.on("oncontext", function (params) {
    params.event.preventDefault();
    var nodeId = network.getNodeAt(params.pointer.DOM);
    if (nodeId) {
      menu.innerHTML = `
        <div><strong>${nodeId}</strong></div>
        <div><a href="https://example.com/${nodeId}" target="_blank">Open wiki page</a></div>
        <div><a href="#" onclick="alert('Expand ${nodeId}'); return false;">Expand department</a></div>
      `;
      menu.style.left = params.pointer.DOM.x + "px";
      menu.style.top = params.pointer.DOM.y + "px";
      menu.style.display = "block";
    } else {
      menu.style.display = "none";
    }
  });

  document.addEventListener("click", function () {
    menu.style.display = "none";
  });
</script>
"""
    
    with open(output_file, "a", encoding="utf-8") as f:
        f.write(javascript)
    print(f"Graph written to {output_file}. Open it in your browser.")
    if __name__ == "__main__":
      os.startfile(output_file)
    f = net.generate_html("output.html",local=True, notebook=False)
    f += javascript
    return f

if __name__ == "__main__":
    G = internal_graph()
    build_graph_visualization(G)
