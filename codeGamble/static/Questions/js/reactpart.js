var LeaderBoard = React.createClass({
    displayName: 'LeaderBoard',

    getInitialState: function () {
        return { list: [] };
    },

    fetchLeaders: function () {
        var ajaxUrl = window.location.origin + this.props.url;
        $.ajax({
            url: ajaxUrl,
            dataType: 'json',
            cache: false,
            success: function (list) {
                this.setState({ list: list });
            }.bind(this),

            error: function (xhr, status, err) {
                console.log(xhr);
            }.bind(this)
        });
    },

    componentDidMount: function () {
        this.fetchLeaders();
        setInterval(this.fetchLeaders, 30000);
    },

    render: function () {
        var list = this.state.list['list'];
        console.log(list);
        if (list !== undefined) {
            return React.createElement(
                'div',
                { className: 'outerBox' },
                React.createElement(
                    'div',
                    { className: 'card grey lighten-5' },
                    React.createElement(
                        'div',
                        { className: 'card-content' },
                        React.createElement(
                            'span',
                            { className: 'card-title' },
                            React.createElement(
                                'h4',
                                null,
                                'Leader Board'
                            )
                        )
                    ),
                    React.createElement(
                        'div',
                        { className: 'card-action' },
                        React.createElement(
                            'ul',
                            { className: 'collection' },
                            list.map(function (obj, index) {
                                return React.createElement(
                                    'li',
                                    { className: 'collection-item', key: index },
                                    obj.id,
                                    '.  ',
                                    obj.name
                                );
                            })
                        )
                    )
                )
            );
        } else {
            return React.createElement('div', null);
        }
    }
});

ReactDOM.render(React.createElement(LeaderBoard, { url: '/questions/leaderboard/get/' }), document.getElementById('leaderboard'));