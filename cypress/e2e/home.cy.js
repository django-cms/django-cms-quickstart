beforeEach(() => {
    const userName = Cypress.env("USERNAME");
    const password = Cypress.env("PASSWORD");

    cy.visit('/');
    cy.login(userName, password);
})

it('Home Page renders properly', () => {
    cy.get('.cms-toolbar-item-logo')
    .should('have.text','django CMS');

    //Static content verification
    cy.get('.cms-welcome-heading')
    .invoke('text')
    .should((text) => {
        const trimmedText = String(text).trim();
        expect(trimmedText).to.equal('Welcome to your new django CMS installation!');
    });
});

it('Home Page interactions work', () => {
    cy.contains('example.com')
        .should('exist');
});