cordova.define('cordova/plugin_list', function(require, exports, module) {
module.exports = [
    {
        "file": "plugins/com.manueldeveloper.speech-recognizer/www/speechrecognizer.js",
        "id": "com.manueldeveloper.speech-recognizer.speechrecognizer",
        "clobbers": [
            "navigator.speechrecognizer"
        ]
    }
];
module.exports.metadata = 
// TOP OF METADATA
{
    "com.manueldeveloper.speech-recognizer": "0.0.1"
}
// BOTTOM OF METADATA
});