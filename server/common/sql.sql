#数据库名字：yishuangxi
drop database if exists yishuangxi;
create database yishuangxi;
use yishuangxi;

#用户表
create table users(
    id int unsigned not null auto_increment primary key,
    username varchar(20) not null unique,
    password varchar(200) not null
) default charset=utf8;

#插入一个默认用户，id=1
insert into users values (1, "yisx", "111");


#博客类别表
create table cates(
    id int unsigned not null auto_increment primary key,
    name varchar(20) not null unique,
    create_time timestamp not null default CURRENT_TIMESTAMP
) default charset=utf8;


#博客文章表blogs
create table blogs (
    id int unsigned not null auto_increment primary key,
    title varchar(20) not null,
    ref_cate int unsigned not null references cates(id),
    content mediumtext not null,
    draft tinyint(1) not null default 0,#只取0和1，0代表不是草稿，1代表是草稿
    pub_time timestamp not null default CURRENT_TIMESTAMP comment "博客发表时间",
    mod_time timestamp not null comment "博客最后修改时间"
) default charset=utf8;


#评论列表comments
create table comments(
    id int unsigned not null auto_increment primary key,
    content varchar(200) not null,
    ref_blog int unsigned not null references blogs(id),
    name varchar(20) default "",
    email varchar(50) default ""
) default charset=utf8;



#创建文章分类view
create view cates_view as
    select
        cates.*,
        (select count(id) from blogs where draft=0 and ref_cate = cates.id) as counts
    from
        cates;

#创建blogs评论view
create view blogs_view as
    select
        blogs.*,
        (select count(id) from comments where ref_blog = blogs.id ) as comment_counts
    from
        blogs;


#插入一个默认分类，id=1
insert into cates values (null, "python", null);
insert into cates values (null, "web", null);
insert into cates values (null, "其他", null);

#插入博客
insert into blogs values(null, "博客标题1", 1, "<h1>博客文章的内容，这是一个大标题</h1><p>这是一个段落</p>",0, null, null);
insert into blogs values(null, "博客标题2", 1, "<h1>博客文章的内容，这是一个大标题</h1><p>这是一个段落</p>",0, null, null);
insert into blogs values(null, "博客标题3", 3, "<h1>博客文章的内容，这是一个大标题</h1><p>这是一个段落</p>",0, null, null);
insert into blogs values(null, "博客标题4", 2, "<h1>博客文章的内容，这是一个大标题</h1><p>这是一个段落</p>",0, null, null);
insert into blogs values(null, "博客标题5", 1, "<h1>博客文章的内容，这是一个大标题</h1><p>这是一个段落</p>",0, null, null);
insert into blogs values(null, "博客标题6", 3, "<h1>博客文章的内容，这是一个大标题</h1><p>这是一个段落</p>",0, null, null);

#插入评论
insert into comments values(null, "这是评论1", 1, "yisx", "yisx@sina.com");
insert into comments values(null, "这是评论2", 6, "yisx", "yisx@sina.com");
insert into comments values(null, "这是评论3", 5, "yisx", "yisx@sina.com");
insert into comments values(null, "这是评论4", 5, "yisx", "yisx@sina.com");
insert into comments values(null, "这是评论5", 4, "yisx", "yisx@sina.com");
insert into comments values(null, "这是评论6", 5, "yisx", "yisx@sina.com");
insert into comments values(null, "这是评论7", 6, "yisx", "yisx@sina.com");
insert into comments values(null, "这是评论8", 1, "yisx", "yisx@sina.com");
insert into comments values(null, "这是评论9", 2, "yisx", "yisx@sina.com");
insert into comments values(null, "这是评论10", 2, "yisx", "yisx@sina.com");
insert into comments values(null, "这是评论11", 3, "yisx", "yisx@sina.com");
insert into comments values(null, "这是评论12", 3, "yisx", "yisx@sina.com");


