



# Earthdaily service status

!!! note "Feedback wanted!"
    The tutorials are a recent addition to our documentation and we are still
    working out what shape they should have in the end. Please [provide any
    feedback you might have in this discussion thread].

    Note, however, that suggestions should be specific and feasible. We want to
    focus on creating more content at the moment, instead of developing a
    specific styling or behaviour for the tutorials. If there are worthwhile
    improvements that we can make through simple customization then we are happy
    to consider those.

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


