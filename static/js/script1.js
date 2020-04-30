
// 获取文档中 class="not select" 的所有元素  也就是不是select的元素
var dls = document.querySelectorAll('dl:not(.select)');
//  获取文档中id = "selector"中的所有元素  也就是放置筛选条件的地方
var selected=document.querySelector('.select');

var tag_special=null;
// 这样传递还是只会出现一点点数据emm  我日了狗了
for (var i = 0; i < dls.length; i++) {
	dls[i].mark=false;	//给每一行的dl标签添加一条属性，用于对应下面的dd标签。我们约定如果这个属性的值为true表示对应的标签没有创建。如果值为false表示对应的标签已经创建了
}

   /* $(document).ready(function(){
        function refresh(){
            $.getJSON("/data_fresh/", function (ret) {
                $('#result').html(ret.data1);

                    })
                }
                setInterval(refresh, 3000)
            })/'*/

   //每个元素都会进行一次select操作，实现价值最大化
function select(n) {
	//  获取dls里面的所有类别  也就是我们所说的tag
	var dds = dls[n].querySelectorAll('dd');
	var prev=null;
	//  下面这个dd就是第三栏的标签出现的变量
	var dd=null;	//每一行都需要创建一个dd标签，放到这里是为了如果标签已经被创建了
	// ，通过这个变量能够找到这个标签
	//
	//data使我们要传递除去的数据
	var data = null;
	for (var i = 0; i < dds.length; i++) {
		//  如果对某一个标签进行了点击，那么久返回，这个click函数居然这么长
		dds[i].onclick = function () {
			//这里是上面的高亮，上面三行的东西
			//给当前点击的添加一个高亮
			//prev && (prev.className = '');

			if(prev){
				prev.className = ''
			}
			//  这个是已经设置好的css样式
			this.className = 'active';
			//  prev是用来标识这个tags是否已经被选过了，也就是tags是否存在最下面的已选条件里面
			prev = this;


			//创建dd标签
			// this是当前元素，parentnode是单数，只有一个父节点  d1节点，是类别
			//  这里还是为了多条件筛选方便
			var parent=this.parentNode;
			if(!parent.mark){	//这个条件满足说明对应的dd标签还没有创建
				// 在对象中创建一个对象，标签为dd
				dd=document.createElement('dd');
				// innerHTML是一个字符串，可以获取内容，这里就是要返回的内容，该怎么搞？
				//  把点击的类别传送到这个新的dd标签里面
				dd.innerHTML=this.innerHTML;
				// appendChild 是在节点的子节点列表末尾添加新节点
				//  这个data是想要传送出去的对象emm
				data = dd.innerText;
				selected.appendChild(dd);
				//  标记这个类别已经完成了选择
				parent.mark=true;

			}else{
				//走这里的时候说明对应的标签已经创建了，只需要把内容修改了就可以了
				//  这一行函数是比较好理解的
				dd.innerHTML=this.innerHTML;
			}
			
			var span=document.createElement('span');
			var This=this;
			//  这个是删除的标志，不太需要我来理解
			span.innerHTML='X';
			span.onclick=function(){
				//alert(1);
				/*
					点击关闭后要做的事情
						1、移除掉dd
						2、把上面点击的那个class去掉
						3、父级身上的mark属性要更新
				 */
				selected.removeChild(dd);
				This.className='';
				parent.mark=false;
			};
			dd.appendChild(span);
		};
	}
}
