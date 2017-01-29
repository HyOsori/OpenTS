/**
 * Created by hch on 2017. 1. 22..
 */

class View_Result_header extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <div className="result_header">
                <div className="container">
                    <div className="result_stock">^1800000</div>
                    <div className="result_title">SAMSUNG</div>
                </div>
            </div>


        )
    }
}

class View_Result_content extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <div className="result_content">
                <div className="container">
                    여기에 내용을 쓰자꾸나
                </div>
            </div>


        )
    }
}
ReactDOM.render(<View_Result_header/>, document.getElementById('titleBar'));
ReactDOM.render(<View_Result_content/>, document.getElementById('content'));