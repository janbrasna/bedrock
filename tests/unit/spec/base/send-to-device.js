/*
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at https://mozilla.org/MPL/2.0/.
 */

/* For reference read the Jasmine and Sinon docs
 * Jasmine docs: https://jasmine.github.io/
 * Sinon docs: http://sinonjs.org/docs/
 */

/* eslint camelcase: [2, {properties: "never"}] */
/* eslint new-cap: [2, {"capIsNewExceptions": ["Deferred"]}] */

import SendToDevice from '../../../../media/js/base/send-to-device.es6';

describe('send-to-device.js', function () {
    let form;

    beforeEach(function () {
        const formMarkup = `<section id="send-to-device" class="send-to-device">
                <div class="form-container">
                    <form class="send-to-device-form" action="https://basket.mozilla.org/news/subscribe/">
                        <p class="mzp-c-form-errors email">Please enter an email address.</p>
                        <p class="mzp-c-form-errors system">An error occurred in our system. Please try again later.</p>
                        <div class="send-to-device-form-fields">
                            <input type="hidden" value="all">
                            <label id="mzp-c-field-label" for="send-to-device-input">Enter your email.</label>
                            <div class="mzp-c-field mzp-l-stretch">
                                <input id="send-to-device-input" class="mzp-c-field-control send-to-device-input" name="s2d-email" type="text" required>
                                <button type="submit" class="button mzp-c-button mzp-t-product">Send</button>
                            </div>
                        </div>
                        <div class="thank-you hidden"><a href="#" role="button" class="send-another">Send to another device</a></div>
                        <div class="loading-spinner"></div>
                    </form>
                </div>
            </section>`;

        document.body.insertAdjacentHTML('beforeend', formMarkup);

        // stub out google tag manager
        window.dataLayer = sinon.stub();
        window.dataLayer.push = sinon.stub();

        form = new SendToDevice();
    });

    afterEach(function () {
        form.unbindEvents();
        const content = document.getElementById('send-to-device');
        content.parentNode.removeChild(content);
    });

    describe('instantiation', function () {
        it('should create a new instance of SendToDevice', function () {
            spyOn(form, 'bindEvents');
            form.init();
            expect(form instanceof SendToDevice).toBeTruthy();
            expect(form.bindEvents).toHaveBeenCalled();
        });
    });

    describe('onFormSubmit', function () {
        let xhrRequests;

        beforeEach(function () {
            xhrRequests = [];

            function FakeXHR() {
                this.headers = {};
                this.readyState = 0;
                this.status = 0;
                this.responseText = '';
                this.onload = null;

                xhrRequests.push(this);
            }

            FakeXHR.prototype.open = jasmine.createSpy('open');
            FakeXHR.prototype.setRequestHeader = function (header, value) {
                this.headers[header] = value;
            };
            FakeXHR.prototype.send = jasmine.createSpy('send');

            spyOn(window, 'XMLHttpRequest').and.callFake(function () {
                return new FakeXHR();
            });
        });

        afterEach(function () {
            xhrRequests = [];
        });

        it('should handle success', function () {
            spyOn(form, 'onFormSuccess').and.callThrough();
            form.init();
            document.getElementById('send-to-device-input').value =
                'foxy@example.com';
            document
                .querySelector('.send-to-device-form button[type="submit"]')
                .click();

            const req = xhrRequests[0];
            req.status = 200;
            req.readyState = 4;
            req.responseText = '{"status": "ok"}';
            req.onload({ target: req });

            expect(form.onFormSuccess).toHaveBeenCalled();
        });

        it('should handle invalid email', function () {
            spyOn(form, 'onFormError').and.callThrough();
            form.init();
            document.getElementById('send-to-device-input').value =
                'invalid@email';
            document
                .querySelector('.send-to-device-form button[type="submit"]')
                .click();

            const req = xhrRequests[0];
            req.status = 400;
            req.readyState = 4;
            req.responseText =
                '{"status": "error", "desc": "Invalid email address"}';
            req.onload({ target: req });

            expect(form.onFormError).toHaveBeenCalledWith(
                'Invalid email address'
            );
        });

        it('should handle failure', function () {
            spyOn(form, 'onFormError').and.callThrough();
            form.init();
            document.getElementById('send-to-device-input').value =
                'ohnoes@example.com';
            document
                .querySelector('.send-to-device-form button[type="submit"]')
                .click();

            const req = xhrRequests[0];
            req.status = 500;
            req.readyState = 4;
            req.responseText = null;
            req.onload({ target: req });

            expect(form.onFormError).toHaveBeenCalled();
        });
    });
});
