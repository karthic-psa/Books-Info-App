$(document).ready(function() {
    let booktitle = $('#btitle').text();
    let urlgbookst = "https://www.googleapis.com/books/v1/volumes?q="+booktitle;
    // let urlWiki = "https://en.wikipedia.org/w/api.php?action=opensearch&search="+text+"&format=json&callback=wikiCallback";
    let timeoutWiki = setTimeout(function(){
    $('#bookdetail').text("wikipedia resources not loaded");}, 8000);
    $.ajax(urlgbookst,{
      dataType: "json",
      success: function(response){
        // console.log(response)
          console.log(response);
         let temp = response.items[0].volumeInfo.description;
          // console.log(temp);
          $('#bookdetail').text(temp);
        // }
        clearTimeout(timeoutWiki);
      }
    });
});
