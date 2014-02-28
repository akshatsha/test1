Welcome {{user}}

<br/>
%for i in array:
<b>{{i}}</b>
%end


<form action="/fav_num" method="POST" >

Please Enter Fav Number
<input type="text" name="fav_num">

<input type="submit">

</form>
