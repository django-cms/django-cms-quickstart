before(() => {

});

it('Log in djangoCMS', () => {
    const userName = Cypress.env("USERNAME");
    const password = Cypress.env("PASSWORD");

    cy.visit('/');

    cy.get('#id_username')
        .type(userName);

    cy.get('#id_password')
        .type(password);

    cy.contains('Log in')
    .click();
});