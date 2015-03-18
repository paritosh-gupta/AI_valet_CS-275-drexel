var CustomPlugin = {};

CustomPlugin.callNativeMethod = function() {
    alert("nononon")
    cordova.exec(null, null, "CustomPlugin", "callNativeMethod", []);
};
