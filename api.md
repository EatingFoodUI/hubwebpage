

**获取ip与当前用户上次登录时间**

~~~
/getUserMation?username=''

{
    ip:''返回xxx的ip地址
    time:''xxx上一次登录的时间
}
/editUserMation
前端传回当前用户登录时间
{
    username:xxxx
    time:'' 用户退出登录的时间
}


~~~



**登录板块**  login页面

（前端传回输入密码和帐号 后台校验返回）

~~~
/checklogin

返回一static
[static:0/1/2]
static:0表示没当前帐号
static:1表示密码输入错误
static:2表示验证成功

~~~



**公共组件 headerNav** 

显示管理员id 由login登录成功后记录在全局vuex状态里 



**项目主页**

要求满屏  每一页最多8个具体的项目

~~~
/getProject?name=''&man=''&time=''
做个分页
限制词由前端传回的项目名称 项目负责人 项目时间 具体页面 
3个词都可为空 也就是/getProject?name=&man=&time=&page=1
返回第一页的内容 默认时间最近的放在最前面
{
    list:[{
        projectName:'',项目名称
        projectMan:'',项目负责人
        howmany:'',阅览人数
        time:'', 项目时间 （可选项为 昨天，最近3天，一周内，一个月内，一个月之前）
        Projectid:''每个项目独特的id
    }] 最多8个
    total:2//返回分页的个数 这里是总共分了2页
}	
请求示例 
/getProject?name='重庆日报'&man=&time=&page=1
返回关于重庆日报的内容，第一页
~~~



**项目分类页**

点击具体项目后进入的页面

https://l1csk0.axshare.com/#g=1&p=2-1_%E9%A1%B9%E7%9B%AE%E5%88%86%E7%B1%BB%E9%A1%B5



所有文章类型暂定4个 

**这里可以下拉不要求满屏**

+ 架构设计
+ 关键问题
+ 技术要点
+ 过程日记

~~~
/getTypeProject?Projectid=xxx
返回关于projectId为xx的项目 下的 四个类型的文章

{
    design:[{
        title:''返回具体文章标题
        content:''返回具体文章内容
        id:1,   文章id 
        type:'design' 表示是项目分类的文章
    }], 返回所有架构设计的文章
    keyissue:[{
         title:''返回具体文章标题
         content:''返回具体文章内容
    	id:2,文章id
    	type:'keyissue' 表示是关键问题的文章
    }], 返回所有关键问题的文章
    point:[{
         title:''返回具体文章标题
         content:''返回具体文章内容
         id:3文章id
         type:'point' 表示是技术要点的文章
    }], 返回技术要点的文章
    process:[{
         title:''返回具体文章标题
         content:''返回具体文章内容
         id:4 文章id
         type:'process' 表示是过程日记的文章
    }] 返回过程日记的文章
}

请求示例 /getTypeProject
~~~



所有文章类型为并行结构  每个文章有自己独立的id  和表示自己文章类型的type





**添加项目页** 

注意 这里要加上 项目名称和项目负责人的input 还有一个保存button 原画没写

https://l1csk0.axshare.com/#g=1&p=2-2_%E6%B7%BB%E5%8A%A0%E9%A1%B9%E7%9B%AE%E9%A1%B5

~~~
点击保存按钮后 将写的项目上传 后台自动为这个项目赋予一个Projectid
/addProject
{
    projectName:'',项目名称
    projectMan:'',项目负责人
    time:'' 当前上传的时间 
}
提交成功后后台返回static 以及添加完成后的projectid
{
	Projectid:''新项目独特的id
	static:1
｝
提交失败返回
｛
	static:0
｝

~~~



**添加/编辑文章页**

在项目分类页点编辑 可进入编辑文章页面

前端传回修改的文章标题与文章内容

~~~
/getProjectPage?ProjectId=xxx&type=&id=   得到文章id为xx并且类型为xx类型的具体的文章

限制词有3个 一个是projectid 必须，表示某某项目 
另外一个是type  表示某某类型 必须
另外一个是id  表示具体的文章id  必须
这样就得到具体某个项目下 某个类型的具体文章了
｛
	type:''文章类型
	id:''文章id
	title:'' 文章标题
    content:''文章内容
｝
编辑后呢 前端发送
｛
	type:''文章类型
	id:''文章id
	title:'' 文章标题
    content:''文章内容
    time:''编辑后的时间
｝

/addProjectPage?Projectid=&type=   为项目名字为xx并且文章类型为xx下添加文章 后台自动给文章赋予id

限制词有2个 一个是projectid 必须，表示某某项目 
另外一个是type  表示某某类型 必须
前端发送
｛
	type:''文章类型
	title:''修改后的文章标题
	content:''文章内容
	time：'' 添加时间
｝
提交成功后 
｛
	
	static:1
｝
提交失败返回
｛
	static:0
｝

~~~





**文章页面**

https://l1csk0.axshare.com/#g=1&p=3_%E6%96%87%E7%AB%A0

之前的项目分类页点进去项目 是看 关于这个**项目** 的文章

这里是看 **所有** 文章   

文章分为两类

+ 一种与项目挂钩的 也就是之前项目页的
+ 一种是这里的 也就是不和项目挂钩的

这里要求**不能下拉**（满屏显示） 每一页最多显示8个文章



~~~
/getAllPage?title=?author=?time=?page=?

限制词有标题 作者 上传时间 以及分页page
｛
	total:20 总共分了多少页
	pageAll:[{
		id:''文章id
         title:''文章标题,
         content:''文章部分内容 返回前20个词就好，
	},] 所有文章 最多8个
｝
~~~

点击 编辑/添加 后 跳转到吴锦洲的  编辑文章与添加文章页面  注与之前那个不同

**编辑/添加文章**

~~~
/getCommonPage?id=   得到具体的文章

｛
	id:''文章id
	title:'' 文章标题
    content:''文章内容  
｝
编辑后 前端发送
｛
	id:''文章id
	title:'' 文章标题
    content:''文章内容
    time:''编辑时间
｝
/addCommonPage    提交完后后台自动添加文章id

前端修改文章内容后向后台提交

｛
	title:''修改后的文章标题
	content:''文章内容
	time:''添加时间
｝
提交成功后 
｛
	static:1
｝
提交失败返回
｛
	static:0
｝
~~~



**成员页**

https://l1csk0.axshare.com/#g=1&p=4_%E6%88%90%E5%91%98

显示所有成员

要求满屏显示 每页最多8个

~~~
/getMember?name=&college=&direction=&page=1


限制词有成员姓名 成员学院 小组方向 以及对应的分页

｛
	total:'' 返回总共分页的多少
	member:[{
	    id:'' 每个成员都有一个独立的id 
        name:''成员姓名,
        college:成员学院
        direction:成员方向
	}] //所有的成员信息 这个数组里每一页最多8项
｝

示例请求  
返回姓名为陈思锐方向为前端的
/getMember?name='陈思锐'&college=&direction='前端'&page=1


~~~



**成员编辑/添加成员**

~~~
成员编辑
/editMember?id=

返回具体id的成员信息

｛
	name:''成员名字
	college:''成员学院
	direction:''成员小组方向
	skill:｛
		language:['','']   //学会的语言
		software:['',''] //学会的软件 
	｝	//个人技能
	experience:'' 个人经历
｝
以上信息 如果没有的就返回空就好 比如如果数据库里没有skill下的language 对应的就返回一个空数组的language就好


/addMember
添加成员

｛
	name:''成员名字
	college:''成员学院
	direction:''成员小组方向
	skill:｛
		language:['','']   //学会的语言
		software:['',''] //学会的软件 
	｝	//个人技能
	experience:'' 个人经历
｝
~~~


















