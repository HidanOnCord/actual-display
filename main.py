from website import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0")
    
    
    #if request.method == 'POST':
    #    global data
    #    data = request.form
    #    request_ = oneRequest(email=data['email'], name=data['name'], message=data['message'])
    #    db.session.add(request_)
    #    db.session.commit()        
    #            
    #    for item, value in data.items():
    #        requests.post("https://discord.com/api/webhooks/1040584398619295756/PZt9A0VhIzKJzvbeBhB0oMJx5Cd7lnPNzXcr1M9O8OsUpxRwtBRWtrxdAMm_4KbmozUD", data={"content":f"`{item}`:  **{value}**"})
    #    return render_template('base.html', data=request_)
    #else:
    #    return render_template('base.html', data=request_)

    


