



# Workflow module

<iframe src="https://geosys.statuspage.io/" width="100%" height="600px" style="border: none;"></iframe>

For more details, visit the [Geosys Status Page](https://geosys.statuspage.io/).



<div id="status-page"></div>

<script>
fetch("https://geosys.statuspage.io/")
  .then(response => response.text())
  .then(html => {
      document.getElementById("status-page").innerHTML = html;
  })
  .catch(error => console.error("Error loading status page:", error));
</script>