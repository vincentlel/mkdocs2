



# Earthdaily service status

<div id="status-page"></div>

<script>
fetch("https://geosys.statuspage.io/")
  .then(response => response.text())
  .then(html => {
      document.getElementById("status-page").innerHTML = html;
  })
  .catch(error => console.error("Error loading status page:", error));
</script>

For more details, visit the [Geosys Status Page](https://geosys.statuspage.io/).