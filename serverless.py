const AWS = require('aws-sdk');
var docClient = new AWS.DynamoDB.DocumentClient();

var tableName = "Santhosh";

exports.handler = (event,context,callback) =>
{
    console.log(event.EmailID)
    var params = {
        TableName : tableName,
        Key:{
            "Email": event.EmailID
        }
    }
    
    docClient.get(params,function(err,data){
        callback(err,data)
    })
};
