from sqlalchemy import (
    Column,
    Integer,
    Text,
    Float,
    ForeignKey,
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class users(Base):
    __tablename__ = 'Users'
    username = Column(Text, primary_key=True)
    password = Column(Text)
    firstname = Column(Text)
    middlename = Column(Text)
    lastname = Column(Text)
    street = Column(Text)
    city =Column(Text)
    state = Column(Text)
    zipcode = Column(Integer)
    residence = Column(Text)
    roomnumber = Column(Text)
    phonenumber = Column(Integer)
    email = Column(Text)
    privileges = Column(Integer)
    trainingvalue = Column(Integer, ForeignKey('TrainingLevels.trainingvalue'))
    administrativevalue = Column(Integer, ForeignKey('AdministrativeStatus.administrativevalue'))
    operationalvalue = Column(Integer, ForeignKey('OperationalStatus.operationalvalue'))
    portablenumber = Column(Integer)
    
    def __init__(self, username, password,firstname,middlename,lastname,street,city,
                 state,zipcode,residence,roomnumber,phonenumber,email,privileges,
                 trainingvalue,administrativevalue,operationalvalue,portablenumber):
        self.username = username
        self.password = password
        self.firstname =firstname
        self.middlename = middlename
        self.lastname = lastname
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.residence = residence
        self.roomnumber = roomnumber
        self.phonenumber = phonenumber
        self.email = email
        self.privileges = privileges
        self.trainingvalue = trainingvalue
        self.administrativevalue = administrativevalue
        self.operationalvalue = operationalvalue
        self.portablenumber = portablenumber
        
class emtcert(Base):
    __tablename__ = 'EMTCertification'
    username = Column(Text, ForeignKey('Users.username'), primary_key=True)
    certnumber = Column(Integer)

    def __init__(self, username,certnumber):
        self.username = username
        self.certnumber = certnumber
        
class certifications(Base):
    __tablename__ = 'Certifications'
    username = Column(Text, ForeignKey('Users.username'), primary_key=True)
    certification = Column(Text, primary_key=True)
    expiration = Column(Text)

    def __init__(self, username,certification,expiration):
        self.username = username
        self.certification = certification
        self.expiration = expiration
        
class operationalstatus(Base):
    __tablename__ = 'OperationalStatus'
    operationalvalue = Column(Integer, primary_key=True)
    status = Column(Text)

    def __init__(self, operationalvalue,status):
        self.operationalstatus = operationalvalue
        self.status = status
        
class administrativestatus(Base):
    __tablename__ = 'AdministrativeStatus'
    administrativevalue = Column(Integer, primary_key=True)
    status = Column(Text)

    def __init__(self, administrativevalue,status):
        self.administrativestatus = administrativevalue
        self.status = status
        
class eboardpositions(Base):
    __tablename__ = 'Position'
    position = Column(Text, primary_key=True)
    username = Column(Text, ForeignKey('Users.username'))

    def __init__(self, position,username):
        self.position = position
        self.username = username
      
class traininglevel(Base):
    __tablename__ = 'TrainingLevels'
    trainingvalue = Column(Integer, primary_key=True)
    traininglevel = Column(Text)
    
    def __init__(self, trainingvalue, traininglevel):
        self.trainingvalue = trainingvalue
        self.traininglevel = traininglevel
        
class privileges(Base):
    __tablename__ = 'Privileges'
    privilegevalue = Column(Integer,ForeignKey('Users.privileges'), primary_key=True)
    privilege = Column(Text)
    
    def __init__(self, privilegevalue,privilege):
        self.privilegevalue = privilegevalue
        self.privilege = privilege