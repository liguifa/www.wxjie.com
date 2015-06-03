var time;
$(document).ready(function(){
	$(".table_tr").click(function(){
		var url=$(this).attr("data-url");
		window.location.href=url;
	});
	$("#login").click(function(){
		$.ajax({
			type:"get",
			url:"/login.html",
			data:{
				username:$("input[name=username]").val(),
				password:$("input[name=password]").val()
			},
			success:function(data)
			{
				$('.login').modal('hide')
				if(data.status)
				{
					$("#message").text("登陆成功！");
					$(".user").html("<div id='user_span'>你好 "+data.username+"</div>")
				}
				else
				{
					$("#message").text("登陆失败！密码或用户名错误");
				}
				$('.status').modal('show');
			}
		});
	});
	$("#register").click(function(){
		$.ajax({
			type:"get",
			url:"/register.html",
			data:{
				username:$("input[name=r_username]").val(),
				password:$("input[name=r_password]").val()
			},
			success:function(data)
			{
				$('.register').modal('hide')
				if(data.status=='0')
				{
					$("#message").text("注册成功！");
					$(".user").html("<div id='user_span'>你好 "+data.username+"</div>")
				}
				else if(data.status=='3')
				{
					$("#message").text("注册失败！用户名已存在");
				}
				else
				{
					$("#message").text("注册失败！用户名或密码过长");
				}
				$('.status').modal('show');
			}
		});
	});
	$("#file-span").click(function(){
		$("#file").trigger("click");
	});
	$("#file").change(function(){
		$("#update_file").trigger("click");
		time=setInterval("updateCall()",100);
		$("#message").text("图片上传中...");
		$('.status').modal('show');
	});
	$(".btn-share").click(function(){
		if(!$.cookie('username'))
		{
			$("#message").text("请先登陆！");
			$('.status').modal('show');
			return 0;
		}
		$("#message").text("提交中...");
		$('.status').modal('show');
		$.ajax({
			type:"post",
			url:"/updateIn.html",
			data:{
				title:$("#book_title").val(),
				image:$("#book_image").val(),
				author:$("#book_author").val(),
				introduction:$("#book_introduction").val(),
				recommend:$("#book_recommend").val(),
				line:$("#book_line").val()
			},
			success:function(data)
			{
				data=eval("("+data+")");
				alert(data);
				if(data.status=="1")
				{
					$("#message").text("提交成功!");
					$('.status').modal('show');
				}
				else
				{
					$("#message").text("提交失败!");
					$('.status').modal('show');
				}
			}
		});
	});
});

function updateCall()
{
	var html=$(window.frames["iframe"].document).find("body").text();
	if(html!="")
	{
		clearInterval(time);
		json=JSON.parse(html);
		if(json.status==1)
		{
			$("#message").text("图片上传成功！");
			$('.status').modal('show');
			$("#book_image").val(json.file);
			$("#book_image").attr("disabled","disabled");
		}
		else
		{
			$("#message").text("图片上传失败！");
			$('.status').modal('show');
		}
	} 
}

function pagination(pageIndex,pageCount,urlTpl)
{
	var html="";
	if(parseInt(pageIndex)==1)
	{
		html+="<li><span><</span></li>";
	}
	else
	{
		html+="<li><a href='"+urlTpl.replace("@",parseInt(pageIndex)-1)+"'><</a></li>";
	}

	var pageMin=1;
	if(parseInt(pageIndex)>=4)
	{
		pageMin=parseInt(pageIndex)-2;
	}

	for(var i=pageMin;i<=parseInt(pageCount)&&i<=parseInt(pageIndex)+4;i++)
	{
		if(i==parseInt(pageIndex))
		{
			html+="<li><span class='active'>"+pageIndex+"</span></li>";
		}
		else
		{
			html+="<li><a href='"+urlTpl.replace("@",parseInt(i))+"'>"+i+"</a></li>";
		}
	}

	if(parseInt(pageIndex)==parseInt(pageCount))
	{
		html+="<li><span>最后一页</span></li>";
		html+="<li><span>></span></li>";
	}
	else
	{
		html+="<li><a href='"+urlTpl.replace("@",parseInt(pageCount))+"'>最后一页</a></li>"
		html+="<li><a href='"+urlTpl.replace("@",parseInt(pageIndex)+1)+"'>></span></li>";
	}

	document.write(html);
}
function search(category)
{
	$("input[name=category]").val(category);
	$("button[type=submit]").trigger("click");
}