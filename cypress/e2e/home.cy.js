it('Assert Home Page', () => {
    const userName = Cypress.env("USERNAME");
    const password = Cypress.env("PASSWORD");

    cy.visit('/');
    cy.login(userName, password);

    cy.get('.cms-toolbar-item-logo')
    .should('have.text','django CMS');
    
    cy.get('.cms-welcome-heading')
    .invoke('text')
    .should((text) => {
        const trimmedText = String(text).trim();
        expect(trimmedText).to.equal('Welcome to your new django CMS installation!');
    });
});