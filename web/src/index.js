const requestOptions = {
        method: 'PUT',
    };
    useEffect(() => {
        if (addName !== '') {
            fetch(('http://localhost:5000/adduser/' + username),requestOptions)
                .then(resp => resp.json())
                .then(response => {
                   if (response > 0) {
                        let link = "Portfolio/"+ response
                        navigate(link)
                    }
                }).catch(resp => {
                console.error(resp);
            });
        }
    });
