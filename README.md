# Daisy-Pelican-Theme
A minimalist theme for Pelican static site generator. It's based on [Patara.](http://patarakirby.aristotheme.com/)  
Since I'm not a designer or something, it's probably messy coded.  
***  

To align a image to right in your post:  
```
![PullRight](put/here/image/link.png)
```  
For responsive video embeds:  
```
<div class='embed-container'><iframe src='https://www.youtube.com/embed//lrDXX3NiVnk' frameborder='0' allowfullscreen></iframe></div>
```  

Most probably, when you set your SITENAME and SITESUBTITLE it won't look good. To fix it change theese:  
*(letter-spacing and text-indent must be same. Set them according to your site.)*  
```
.header .logo h1 {
    letter-spacing: 2.45rem;
    text-indent: 2.45rem;
}

.header .logo h6 {
    letter-spacing: 1.5rem;
    text-indent: 1.5rem;
}
```  
 ***  

#### Preview
![Preview](/Preview-1.png)
![Preview](/Preview-2.png)
![Preview](/Preview-3.png)
![Preview](/Preview-4.png)
