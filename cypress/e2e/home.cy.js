it('Assert Home Page', () => {
    const userName = Cypress.env("USERNAME");
    const password = Cypress.env("PASSWORD");

    cy.visit('/');
    cy.login(userName, password);

    cy.get('.cms-toolbar-item-logo')
    .should('have.text','django CMS');

});