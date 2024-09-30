import qpy #qpython运行环境的一些变量可以在这里找到
import androidhelper #sl4a的对象在这个包里
import urllib.request as ur #做外部请求的时候需要
from qsl4ahelper.fullscreenwrapper2 import *

class MainScreen(Layout):
   def __init__(self):
       #开始写XML语言
       super(MainScreen,self).__init__(str("""<?xml version="1.0" encoding="utf-8"?>
<!-- “LinearLayout”线性布局 -->
<!-- 将orientation属性值设置成为horizontal，控件将从水平方向从左往右排列 -->
<!-- 将orientation属性值设置成为vertical,控件将从垂直方向从上往下排列 -->
<!-- “layout_weight”其作用是分配线性布局中的剩余空间到该控件上。 -->
<!-- 在控件没有添加layout_weight属性时，控件未占满线性布局的区域会空出来。 -->
<!-- 设有两个按钮，Button1 和Button2 -->
<!-- 给控件button2加上android:layout_weight="1"后，会把线性布局剩余空间全部占满。 -->
<!-- 如果给button1和button2都加上android:layout_weight="1"，则两个控件均匀分配剩余空间。 -->
<LinearLayout
android:layout_width="fill_parent"
android:layout_height="fill_parent"
android:background="#ff0E4200"
android:orientation="vertical"
xmlns:android="http://schemas.android.com/apk/res/android">
<!-- 1  整句话的作用是声明命名空间的引用。 -->
<!-- 2  xmlns是xml namespace的缩写，意思是xml命名空间。 -->
<!-- 3  xmlns:android中的android是给引用起的名字，这样就可以用android:XXX="......"形式进行操作。这个是可以换成别的名称而不用 android， -->
<!-- 4  后面schemas的意思是xml文件的约束（也就是xml的书写规范，类似于模板），还有一种xml约束是DTD，但schemas相对于DTD来说克服了DTD的局限性，扩展性强。 -->

<!-- 下面是一些控件 -->
<!-- “view”视图 -->
<!-- 图像视图，用于展示图片 -->

<!--<ImageView
android:id="@+id/logo"
android:layout_width="fill_parent"
android:layout_height="0px"
android:layout_weight="10"
  />
-->

<!-- 嵌套水平布局 -->
<LinearLayout
android:layout_width="fill_parent"
android:layout_height="0px"
android:orientation="horizontal"
android:layout_weight="20">
<!-- 用来显示文本的 -->
<!-- 文本框 -->
<TextView
android:layout_width="fill_parent"
android:layout_height="fill_parent"
android:textSize="8dp"
android:text="Hello, QPython"
android:textColor="#ffffffff"
android:layout_weight="1"
android:gravity="center"
    />
</LinearLayout>
<!-- 第一个水平布局结束 -->
<ListView
android:id="@+id/data_list"
android:layout_width="fill_parent"
android:layout_height="0px"
android:layout_weight="55"/>
<!-- 又一个嵌套水平布局 -->
<LinearLayout
android:layout_width="fill_parent"
android:layout_height="0px"
android:orientation="horizontal"
android:layout_weight="8">
<!-- 创建和绘制按钮 -->
<Button
android:layout_width="fill_parent"
android:layout_height="fill_parent"
android:text="load"
android:id="@+id/but_load"
android:textSize="8dp"
android:background="#ffEFC802"
android:textColor="#ffffffff"
android:layout_weight="1"
android:gravity="center"/>
<!-- 第二个按钮 -->
<Button
android:layout_width="fill_parent"
android:layout_height="fill_parent"
android:text="exit"
android:id="@+id/but_exit"
android:textSize="8dp"
android:background="#ff06AF00"
android:textColor="#ffffffff"
android:layout_weight="1"
android:gravity="center"/>
</LinearLayout>
<!-- 第二个嵌套水平布局结束 -->
</LinearLayout>
<!-- 总垂直布局结束 -->
"""),"002.py")#前者设置布局，后者设置窗口名称
#XML语言结束，以下为Python语言
   def on_show(self):
       #生成两个按钮的事件
       self.views.but_exit.add_event(click_EventHandler(self.views.but_exit, self.exit))
       self.views.but_load.add_event(click_EventHandler(self.views.but_load, self.load))

       pass


   #def on_close(self):
       #pass

   def load(self, view, dummy):
       #设置load按钮的事件
       droid = FullScreenWrapper2App.get_android_instance()
       droid.makeToast("Load")#在屏幕上显示提示

       saved_logo = qpy.tmp+"/qpy.logo"
       ur.urlretrieve("http://www.qpython.com.cn/img/img_logo.png", saved_logo)
       self.views.logo.src = "file://"+saved_logo

   def exit(self, view, dummy):
       #设置exit按钮的事件
       droid = FullScreenWrapper2App.get_android_instance()
       droid.makeToast("Exit")#在屏幕上显示提示
       FullScreenWrapper2App.close_layout()



if __name__ == '__main__':
    droid = androidhelper.Android()

    FullScreenWrapper2App.initialize(droid)
    FullScreenWrapper2App.show_layout(MainScreen())
    FullScreenWrapper2App.eventloop()