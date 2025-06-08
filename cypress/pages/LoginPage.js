class LoginPage {
    
    visit() {
        cy.visit('/');
    }

    fillUsername(username) {
        cy.get('#id_username').type(username);
    }

    fillPassword(password) {
        cy.get('#id_password').type(password);
    }

    submit() {
        cy.contains('Log in').click();
    }
}

export default new LoginPage();