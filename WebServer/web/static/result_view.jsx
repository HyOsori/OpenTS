/**
 * Created by hch on 2017. 1. 22..
 */

class View_Result extends React.Component
{
    constructor(props)
    {
        super(props);
    }

    render()
    {
        return (
            <div className="result_background">
                <p>SAMSUNG</p>
            </div>
        )
    }
}

ReactDOM.render(<View_Result/>, document.getElementById('content'));