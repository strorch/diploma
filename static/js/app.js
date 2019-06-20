class App
{
    constructor()
    {
        this.filmManipulation = new FilmManipulation();
    }

    init_read_text()
    {
        let find_butt = document.getElementById('file_input');
        find_butt.onchange = this.filmManipulation.sendFile;
    }

    init()
    {
        this.init_read_text();
    }
}