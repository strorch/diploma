class FilmManipulation
{
    sendFile(e)
    {
        let file = e.target.files;
        let data = new FormData();
        data.append('files', file[0]);
        // console.log(file);
        fetch('/load_file', {
                method: 'POST',
                body: data
            })
            .then(response => {
                return response.json();
            })
            .then(e => {
                console.log(e);
            })
        ;
    }
}