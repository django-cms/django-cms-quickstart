it('Log in djangoCMS', () => {
    const userName = Cypress.env("USERNAME");
    const password = Cypress.env("PASSWORD");

    cy.visit('/');

    cy.get('#branding h1')
    .should('have.text','Django administration');

    cy.login(userName, password);
});