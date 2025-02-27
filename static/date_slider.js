// static/date_slider.js

$(document).ready(function() {
    // ===== SLIDER FOR TAB A (Single Stock Chart) =====
    var minDateA = new Date(2000, 0, 1).getTime();  // Jan 1, 2020
    var maxDateA = new Date().getTime();            // Today's date
  
    $("#date_range").ionRangeSlider({
      type: "double",
      grid: true,
      min: minDateA,
      max: maxDateA,
      from: minDateA,
      to: maxDateA,
      prettify: function(num) {
        var date = new Date(num);
        return date.toISOString().split('T')[0];
      },
      onFinish: function(data) {
        $("#start_date").val(new Date(data.from).toISOString().split('T')[0]);
        $("#end_date").val(new Date(data.to).toISOString().split('T')[0]);
      }
    });
  
    // Initialize hidden fields on page load for Tab A
    var sliderA = $("#date_range").data("ionRangeSlider");
    $("#start_date").val(new Date(sliderA.result.from).toISOString().split('T')[0]);
    $("#end_date").val(new Date(sliderA.result.to).toISOString().split('T')[0]);
  
  
    // ===== SLIDER FOR TAB B (Compare Stocks) =====
    var minDateB = new Date(2000, 0, 1).getTime();
    var maxDateB = new Date().getTime();
  
    $("#date_range_compare").ionRangeSlider({
      type: "double",
      grid: true,
      min: minDateB,
      max: maxDateB,
      from: minDateB,
      to: maxDateB,
      prettify: function(num) {
        var date = new Date(num);
        return date.toISOString().split('T')[0];
      },
      onFinish: function(data) {
        $("#start_date_compare").val(new Date(data.from).toISOString().split('T')[0]);
        $("#end_date_compare").val(new Date(data.to).toISOString().split('T')[0]);
      }
    });
  
    // Initialize hidden fields on page load for Tab B
    var sliderB = $("#date_range_compare").data("ionRangeSlider");
    $("#start_date_compare").val(new Date(sliderB.result.from).toISOString().split('T')[0]);
    $("#end_date_compare").val(new Date(sliderB.result.to).toISOString().split('T')[0]);
  });
  