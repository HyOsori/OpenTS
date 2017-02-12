/**
 * Created by hch on 2017. 1. 22..
 */

class View_Search extends React.Component
{
    constructor(props)
    {
        super(props);

        this.on_button_click = this.on_button_click.bind(this);
    }

    on_button_click()
    {
        window.location = "/web/result?keyword=" + $('#search_input').val();
    }

    render()
    {
        return (

            <div className = "search_back">

                <input className = "search_input" id="search_input">
                </input>
                <button type="submit" onClick={this.on_button_click} className = "search_btn">
                    <span> ☌ </span>
                </button>

            </div>

            /*<div className="search_background">
                <input className="search_bar">

                </input>

                <div className="search_btn">

                </div>
            </div>*/
        )
    }
}

ReactDOM.render(<View_Search/>, document.getElementById('contents'));