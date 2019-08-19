var no_of_table = {{no_of_table}}; //Same as below
var list_len_last = {{list_len_last}}; //Same as below
var dict_table = {{dict_table|safe}}; //Here, the error is because the single quote is not put so that this would be a dictionary and not a string
var column_no = {{column_no}};
var length;
var length_first;
var cell = [];


function table_func(i) 
{

    var table = document.getElementById("list_table");
    
    //This below code deletes the row that is already being seen on the screen to make the table empty, so new rows are filled. Uses the length variable previous value, thus this function's placing is important.
    for(var d = 0; d < (length); d++)
    {
        var row_del = table.deleteRow(length-d);
    };
    
    if(i == no_of_table){length = list_len_last;} else{length = 20;}; //Preperation for the different number of rows for last page

    for(var j=0; j < length; j++)
    {
        var row = table.insertRow(-1);

        for(var k=0; k < column_no; k++)
        {
            cell[k] = row.insertCell(k);
            cell[k].innerHTML = dict_table[i][j][k];
        };

    };
};
function table_first()
{
    //This is the table_func() just without delete row capability, thus it displayes the rows in an empty table

    var table = document.getElementById("list_table");

    if(1 == no_of_table){length_first = list_len_last;} else{length_first = 20;}; //This line is in case the order list is smaller then 20 rows

    length = length_first; //This gives the table_func() initial number of rows that it has to delete so that the table is empty again 

    for(var j=0; j < length_first; j++)
    {
        var row = table.insertRow(-1);

        for(var k=0; k < column_no; k++)
        {
            cell[k] = row.insertCell(k);
            cell[k].innerHTML = dict_table[1][j][k];
        };

    };
};
window.onload = table_first;