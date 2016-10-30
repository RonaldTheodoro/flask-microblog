function set_openid (openid, provider) {
    username = openid.search ('<username>');
	if (username != -1) {
	    // openid requires username
		user = prompt('Enter your ' + provider + ' username: ');
		openid = openid.substr (0, username) + user;
	}
	form = document.forms['login'];
    form.elements['openid'].value = openid;
}