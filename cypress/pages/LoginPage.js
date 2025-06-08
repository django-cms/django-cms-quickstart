class LoginPage {

    visit() {
        cy.visit('/');
    }

    fillUsername(username) {
        cy.get('#id_username').type(username, { log: false });
    }

    fillPassword(password) {
        cy.get('#id_password').type(password, { log: false });
    }

    submit() {
        cy.contains('Log in').click();
    }
}

export default new LoginPage();