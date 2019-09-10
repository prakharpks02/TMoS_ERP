var no_of_days = {{no_of_days}};
var day_record = {{day_record}};
var date_keys = object.keys(day_record);

function driver_past()
{
    var table = document.getElementById("driver_record");
    for(var i=0; i<no_of_days;i++)
    {
        var row = table.insertRow(-1);
        row.insertCell(0).innerHTML = date_keys[i];
        row.insertCell(1).innerHTML = day_record[date_keys[i]];
    }
}

window.onload = driver_past;