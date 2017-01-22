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
                <p className="result_bar">SAMSUNG</p>
                <p className="result_stock">^1800000</p>
                <a className="result_detail">6시간 전(2016/01/18 - 13:48:27) 갱신된 자료입니다.</a>
            </div>
        )
    }
}

ReactDOM.render(<View_Result/>, document.getElementById('content'));