var LeaderBoard = React.createClass({
    getInitialState: function(){
        return {list:[]};
    },
    
    fetchLeaders: function(){
        var ajaxUrl = window.location.origin+this.props.url;
        $.ajax({
            url: ajaxUrl,
            dataType: 'json',
            cache: false,
            success: function(list){
                this.setState({list:list});
            }.bind(this),
            
            error: function(xhr, status, err) {
                console.log(xhr);
            }.bind(this),
        });
    },
    
    componentDidMount: function(){
        this.fetchLeaders();
        setInterval(this.fetchLeaders,30000);
    },
    
    render: function(){
        var list = this.state.list['list'];
        console.log(list)
        if(list !== undefined){
            return (
                <div className="outerBox">
                    <div className="card grey lighten-5">
                        <div className="card-content">
                            <span className="card-title">
                                <h4>Leader Board</h4>
                            </span>
                        </div>
                        <div className="card-action">
                            <ul className="collection">
                            {list.map(function(obj, index){
                                return <li className="collection-item" key={ index }>{obj.id}.&nbsp;&nbsp;{obj.name}</li>;
                            })}
                            </ul>
                        </div>
                    </div>
                </div>
            );
        }
        else{
            return(<div></div>);
        }
    },
});

ReactDOM.render(<LeaderBoard url="/questions/leaderboard/get/"/>,document.getElementById('leaderboard'));