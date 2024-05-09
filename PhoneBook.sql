Create database phonebook

Create table person
(personid char(10) constraint PK_person_personid primary key,
 name varchar(50) not null,
 email varchar(60) null 
);

Create table phone
(PersonID char(10) constraint FK_phone_personid references person(personid) not null,
 phone varchar(13) not null
);

Create table groups
(groupid serial constraint PK_groups_groupid primary key,
 title varchar(20) not null
);

Create table persongroup
(personid char(10) constraint FK_persongroup_personid references person(personid) not null,
 groupid int constraint FK_persongroup_groupid references groups(groupid)
);
insert into person() values()