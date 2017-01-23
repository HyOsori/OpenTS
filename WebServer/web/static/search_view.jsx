/**
 * Created by hch on 2017. 1. 22..
 */

class View_Search extends React.Component
{
    constructor(props)
    {
        super(props);
    }

    render()
    {
        return (

            <div className = "search_back">

                <input className = "search_input">
                </input>

                <form action = "/web/result">
                  <button type="submit" className = "search_btn">
                    <span> ☌ </span>
                  </button>
                </form>

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