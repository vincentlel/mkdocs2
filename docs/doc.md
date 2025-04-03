# Earthdaily service status

<div id="statuspage-container"></div>

<script>
  async function fetchStatus() {
    const pageId = "geosys"; // Replace with your actual Statuspage ID
    const url = `https://${pageId}.statuspage.io/api/v2/status.json`;

    try {
      const response = await fetch(url);
      const data = await response.json();
      document.getElementById("statuspage-container").innerHTML = `
        <div style="background: ${data.status.indicator === 'none' ? 'green' : 'red'}; 
                    color: white; padding: 10px; border-radius: 5px;">
          <strong>Status:</strong> ${data.status.description}
        </div>
      `;
    } catch (error) {
      console.error("Error fetching status:", error);
    }
  }

  fetchStatus();
</script>

<html>
<body>
    <!-- Statuspage Embed -->
    <div data-id="geosys" data-host="your-statuspage-domain" class="statuspage-widget"></div>
    <script src="https://geosys.betteruptime.com/embed/script.js"></script>

</body>
</html>

For more details, visit the [Geosys Status Page](https://geosys.statuspage.io/).


