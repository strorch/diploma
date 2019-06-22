$(document).ready(function(){
    $('select').formSelect();

    // $('input[type=file]').change(function (ev) {
    //     var file = ev.target.files;
    //     var data = new FormData();
    //     data.append('files', file[0]);
    //     // console.log(file);
    //     $.ajax({
    //         type: "POST",
    //         url: "/load_file",
    //         data: data,
    //         success: function () {
    //             $('#message').html("<h2>Contact Form Submitted!</h2>")
    //         }
    //     });
    //     console.log(this.files[0].mozFullPath, data);
    // });
});