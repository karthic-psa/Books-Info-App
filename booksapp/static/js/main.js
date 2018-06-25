let menu = document.querySelector('#menu');
      let main = document.querySelector('main');
      let drawer = document.querySelector('.nav');
      menu.addEventListener('click', function(e) {
        drawer.classList.toggle('open');
        e.stopPropagation();
      });
      main.addEventListener('click', function() {
        drawer.classList.remove('open');
      });
let slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
  showSlides(slideIndex += n);
}

function currentSlide(n) {
  showSlides(slideIndex = n);

}

function showSlides(n) {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  let dots = document.getElementsByClassName("demo");
  let captionText = document.getElementById("caption");

  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "flex";
  dots[slideIndex-1].className += " active";
  captionText.innerHTML = dots[slideIndex-1].alt;
}

$(document).on("click", ".open_BookDialog", function () {
     // let myBookId = $(this).data('id');
    let tempele = $(this);
    let timgitem = tempele.find('img').attr('src');
    let booktitle = tempele.find('h3').text();
    let mdesc = tempele.find('p').text();
    // let bookid = $(this).attr('data-internalid');
     $("#myModalLabel").text(booktitle);
     $("#modalImage").attr('src',timgitem);
     $('#book_desc').text(mdesc);
//     let urlmbooks = "https://www.googleapis.com/books/v1/volumes?q="+booktitle;
//          let timeoutWiki = setTimeout(function(){
//       $('#book_desc').text("wikipedia resources not loaded");}, 8000);
//     $.ajax(urlmbooks,{
//       dataType: "json",
//       success: function(response){
//
//          let temp = response.items[0].volumeInfo.description;
//           // console.log(temp);
//
//         // let gbooksList = response[1];
//         // for (let i=0; i< wikiList.length;i++){
//         //   strWiki = wikiList[i];
//         //   let link = 'http://en.wikipedia.org/wiki/'+strWiki;
//           $('#book_desc').text(temp);
//
//         // }
//         clearTimeout(timeoutWiki);
//       }
//     });
//      // $(".open_details").attr('href', "{% url 'details' "+bookid);
//     // console.log(booktitle);
//     // console.log(bookid);
//     let urlgbooks = "https://www.googleapis.com/books/v1/volumes?q="+booktitle;
//      // As pointed out in comments,
//      // it is superfluous to have to manually call the modal.
//      // $('#addBookDialog').modal('show');
// });

// $(document).on("click", ".open_details", function () {
//      // let myBookId = $(this).data('id');
//     let booktitle = $(this).text()
//      $("#myModalLabel").text(booktitle);
//     console.log(booktitle)
//      // As pointed out in comments,
//      // it is superfluous to have to manually call the modal.
//      // $('#addBookDialog').modal('show');
// });
// $(document).on("click", function () {
//     $("#myModalLabel").append('');
});

$(document).ready(function() {
  $('.snippet').each(function() {
    let item = $(this);
    let text = item.find('h3').text();
    let urlgbooks = "https://www.googleapis.com/books/v1/volumes?q="+text;
    // let urlWiki = "https://en.wikipedia.org/w/api.php?action=opensearch&search="+text+"&format=json&callback=wikiCallback";
    let timeoutWiki = setTimeout(function(){
      item.find('p').text("wikipedia resources not loaded");}, 8000);
    $.ajax(urlgbooks,{
      dataType: "json",
      success: function(response){
        // console.log(response)
          console.log(response)
         let temp = response.items[0].volumeInfo.description;
          // console.log(temp);

        // let gbooksList = response[1];
        // for (let i=0; i< wikiList.length;i++){
        //   strWiki = wikiList[i];
        //   let link = 'http://en.wikipedia.org/wiki/'+strWiki;
          item.find('p').text(temp);

        // }
        clearTimeout(timeoutWiki);
      }
    });

  });
});
function searchFunction() {
    let input, filter, ul, li, a, i;
    input = document.getElementById("myInput");
    filter = input.value.toUpperCase();
    ul = document.getElementById("books_ul");
    li = ul.getElementsByTagName("li");
    for (i = 0; i < li.length; i++) {
        a = li[i].getElementsByTagName("h2")[0];
        if (a.innerHTML.toUpperCase().indexOf(filter) > -1) {
            li[i].style.display = "";
        } else {
            li[i].style.display = "none";

        }
    }
}
function searchFunctionLang() {
    let input, filter, ul, li, a, i;
    input = document.getElementById("myInputLang");
    filter = input.value.toUpperCase();
    ul = document.getElementById("langList");
    li = ul.getElementsByTagName("li");
    for (i = 0; i < li.length; i++) {
        a = li[i].getElementsByTagName("a")[0];
        if (a.innerHTML.toUpperCase().indexOf(filter) > -1) {
            li[i].style.display = "";
        } else {
            li[i].style.display = "none";

        }
    }
}
function searchFunctionAuth() {
    let input, filter, ul, li, a, i;
    input = document.getElementById("myInputAuth");
    filter = input.value.toUpperCase();
    ul = document.getElementById("authList");
    li = ul.getElementsByTagName("li");
    for (i = 0; i < li.length; i++) {
        a = li[i].getElementsByTagName("a")[0];
        if (a.innerHTML.toUpperCase().indexOf(filter) > -1) {
            li[i].style.display = "";
        } else {
            li[i].style.display = "none";

        }
    }
}