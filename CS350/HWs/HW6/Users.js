const Model = Sequelize.Model;
class Users extends Model {}
Users.init({
    id: Sequelize.INTEGER,
    email: Sequelize.STRING,
    password : Sequelize.STRING,
    resturantOwner: Sequelize.BOOLEAN
}, {sequelize, modelName: 'Users'});