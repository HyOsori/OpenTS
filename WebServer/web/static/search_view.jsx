/**
 * Created by hch on 2017. 1. 22..
 */

class View_Search extends React.Component
{
    constructor(props)
    {
        super(props);

        this.on_button_click = this.on_button_click.bind(this);
        this.checkEnter = this.checkEnter.bind(this);
    }

    on_button_click()
    {
        // window.location = "/web/getshcode?keyword=" + $('#search_input').val();

        $.get( "http://localhost:8000/web/getshcode?keyword=" + $('#search_input').val(),
            function( response )
            {
                var shcode = response['shcode'];
                if(shcode == -1){
                    alert('존재하지 않는 종목입니다');
                }
                else{
                    window.location = "/web/result?keyword=" + shcode;
                }

            });

    }

    checkEnter(e){

        if(e.keyCode == 13){
            this.on_button_click();
        }

    }

    render()
    {
        return (

            <div className = "search_back">

                <input className = "search_input" onKeyDown={this.checkEnter} id="search_input">
                </input>
                <button type="submit" onClick={this.on_button_click} className = "search_btn">
                    <span> ☌ </span>
                </button>

            </div>
        )
    }
}

ReactDOM.render(<View_Search/>, document.getElementById('contents'));