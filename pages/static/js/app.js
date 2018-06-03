var options = {
  auth: {
    redirectUrl: AUTH0_CALLBACK_URL,
    responseType: 'code',
    params: {
      scope: 'openid profile'
    }
  },
  socialButtonStyle: 'small',
  theme: {
    //logo: 'https://scontent-frx5-1.xx.fbcdn.net/v/t1.0-9/18193780_1929270887309541_6762038252907726006_n.png?oh=5c9629777f338cbe79a11d07c42e97cd&oe=5AB444B9',
    primaryColor: '#31324F'
  },
  languageDictionary: {
    title: "Oqtor"
  },
};

var lock = new Auth0Lock(AUTH0_CLIENT_ID, AUTH0_DOMAIN, options);
