const By = require('selenium-webdriver').By;

class HomePage {
    constructor(driver) {
        this.driver = driver;
        this.locators = {
            inviteeForm: By.id("registrar"),
            inviteeNameField: By.css("#registrar input[name='name']"),
            tog_non_respond_vis: By.css('.main > div input'),
            rem_btn_invitee: invitee => By.xpath(`//span[text() = "${invitee}"]/../button[last()]`)
        };
    }

    open() {
        this.driver.get(process.env.URL);
    }

    addInvitee(name) {
        this.driver.findElement(this.locators.inviteeNameField)
            .sendKeys(name);
        this.driver.findElement(this.locators.inviteeForm).submit();
    }

    rem_invitee(name) {
        this.driver.findElement(this.locators.rem_btn_invitee(name))
        .click();
    }

    tog_non_respond_vis() {
        this.driver.findElement(this.locators.tog_non_respond_vis)
        .click();
    }

}

module.exports = HomePage;
