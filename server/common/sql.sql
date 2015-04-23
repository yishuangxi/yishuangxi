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
    name varchar(20) not null unique
) default charset=utf8;

#插入一个默认分类，id=1
insert into cates values (1, "其他");


#博客文章表blogs
create table blogs (
    id int unsigned not null auto_increment primary key,
    title varchar(20) not null,
    ref_cate int unsigned not null references cates(id),
    content mediumtext not null,
    pub_time timestamp not null default CURRENT_TIMESTAMP comment "博客发表时间",
    mod_time timestamp not null comment "博客最后修改时间"
) default charset=utf8;

#插入一篇博客
insert into blogs values(1, "博客标题1", 1, "<h1>博客文章的内容，这是一个大标题</h1><p>这是一个段落</p>", null, null);
insert into blogs values(null, "博客标题2", 1, "<h1>博客文章的内容，这是一个大标题</h1><p>这是一个段落</p>", null, null);


#评论列表comments
create table comments(
    id int unsigned not null auto_increment primary key,
    content varchar(200) not null,
    ref_blog int unsigned not null references blogs(id),
    name varchar(20) default "",
    email varchar(50) default ""
) default charset=utf8;




