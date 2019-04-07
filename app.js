class NavigatorProxyHandler {

  constructor () {
    this._language = navigator.language;
  }

  set (obj, prop, val) {
    if (prop === 'language') {
      this._language = val;
    }
  }

  get (obj, prop) {
    if (prop === 'language') {
      return this._language;
    }
  }
};

let navigatorProxy = new Proxy(navigator, new NavigatorProxyHandler());
