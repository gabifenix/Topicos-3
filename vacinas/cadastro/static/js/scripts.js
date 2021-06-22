$(document).ready(function(){
    $('.delete-btn').live('click', function() {
       var deleteBtn = confirm('Deseja realmente realizar a exclusão?');
       if (deleteBtn){
          window.location = $(this).attr('href');
       }
       return false;
    });
});