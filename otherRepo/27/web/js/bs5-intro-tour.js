function Tour(steps, options) {
    this.options = options || {};
    this.currentTab = 0;
    this.steps = steps;

    //HTML elements container
    this.elements = {};

    //Helper which works similar to $.extend
    this.extend = function(a, b) {
        for (var key in b)
            if (b.hasOwnProperty(key))
                a[key] = b[key];
        return a;
    }

    var defaultTranslations = {
        next: "Next",
        previous: "Previous",
        finish: "Finish"
    };

    var getPopoverSettings = function(arrows) {
        var template = '<div id="tour" class="popover popover-tour" role="tooltip">' +
            '<div class="popover-arrow"></div>';
        if (!arrows) {
            template = '<div id="tour" class="popover popover-tour popover-tour-center" role="tooltip">';
        }

        template += '<div class="tour-exit"></div>' +
            '<h3 class="popover-header"></h3>' +
            '<div class="popover-body">' +
            '</div>' +
            '<div class="popover-footer">' +
            '   <a class="btn tour-prev">' +
            translations.previous +
            '   </a>' +
            '   <a class="btn tour-next">' +
            translations.next +
            '   </a>' +
            '   <a class="btn btn-primary tour-finish hidden">' +
            translations.finish +
            '   </a>' +
            '</div>' +
            '</div>';

        return {
            placement: "auto",
            template: template,
            trigger: "manual",
            html: true,
            sanitize: false
        };
    }

    var translations = this.extend(defaultTranslations, this.options.translations);
    this.defaultOptions = {
        popoverNoArrows: getPopoverSettings(false),
        popover: getPopoverSettings(true)
    }
}

Tour.prototype.getCurrentStepContent = function() {
    return this.steps[this.currentTab].content;
}

Tour.prototype.getCurrentStepTitle = function() {
    return this.steps[this.currentTab].title || "";
}

Tour.prototype.createTabLinks = function() {
    var html = '<ul class="tour-tab-links">';

    for (var i = 0; i < this.steps.length; i++) {
        var cssClass = i === 0 ? "active" : "";
        html += '<li><a role="button" class="' + cssClass + '" data-tour-step="' + i + '">'+i+'</a></li>';
    }

    html += '</ul>';
    return html;
}

Tour.prototype.createContent = function() {
    var content = this.getCurrentStepContent();
    content += this.createTabLinks();
    return content;
}

Tour.prototype.addBackdrop = function() {
    var backdrop = document.getElementsByClassName("modal-backdrop");

    if (backdrop.length === 0) {
        var body = document.getElementsByTagName("body")[0];
        var backdropElement = document.createElement('div');
        backdropElement.classList.add("modal-backdrop", "show");
        body.appendChild(backdropElement);

    }
}

Tour.prototype.removeBackdrop = function() {
    var backdrop = document.getElementsByClassName("modal-backdrop");

    if (backdrop.length > 0) {
        backdrop[0].remove();

    }
}

Tour.prototype.getContainerByIndex = function(index) {
    var tourPopover = document.getElementsByTagName("body")[0];
    if (this.steps[index].id) {
        tourPopover = document.getElementById(this.steps[index].id);
    }
    return tourPopover;
}

Tour.prototype.getDefaultPopoverSettings = function() {
    var container = this.getContainerByIndex(this.currentTab);
    if (container.tagName.toLowerCase() === "body") {
        return this.defaultOptions.popoverNoArrows;
    } else {
        return this.defaultOptions.popover;
    }
}

Tour.prototype.show = function() {
    this.addBackdrop();

    var opt = {};

    opt = this.extend(this.getDefaultPopoverSettings(), this.options.popover || {});

    opt.title = this.getCurrentStepTitle();
    opt.content = this.createContent();

    var tourPopover = this.getContainerByIndex(this.currentTab);
    var popover = new bootstrap.Popover(tourPopover, opt);

    popover.show();
    var o = this;
    var e = {
        btnNext: popover.tip.getElementsByClassName("tour-next")[0],
        btnPrev: popover.tip.getElementsByClassName("tour-prev")[0],
        btnFinish: popover.tip.getElementsByClassName("tour-finish")[0],
        btnExit: popover.tip.getElementsByClassName("tour-exit")[0]
    };

    //Init events
    e.btnNext.addEventListener("click", function() {
        o.refreshTab(o.currentTab + 1);
    });
    e.btnPrev.addEventListener("click", function() {
        o.refreshTab(o.currentTab - 1);
    });

    var onExit = function() {
        o.removeBackdrop();
        o.removeActiveElement();
        o.popover.dispose();
    }
    e.btnFinish.addEventListener("click", function() {
        onExit();
    });

    e.btnExit.addEventListener("click", function() {
        onExit();
    });
    var tabLinks = popover.tip.getElementsByClassName("tour-tab-links")[0].getElementsByTagName("a");
    for (var i = 0; i < tabLinks.length; i++) {
        tabLinks[i].addEventListener("click",
            function() {
                var step = parseInt(this.dataset.tourStep);
                o.refreshTab(step);
            });
    }
    this.popover = popover;
    this.elements = e;

    this.updateButtonsVisibility();
    this.updateActiveElement();
}

//Moves current HTML element before backdrop (by changing z-index)
Tour.prototype.updateActiveElement = function() {

    for (var i = 0; i < this.steps.length; i++) {
        var e = this.getContainerByIndex(i);;

        if (i === this.currentTab) {
			e.scrollIntoView();
            e.classList.add("tour-active-element");
        } else {
            e.classList.remove("tour-active-element");
        }

    }
}

Tour.prototype.removeActiveElement = function() {
    this.currentTab = -1;
    this.updateActiveElement();
    this.currentTab = 0
}

Tour.prototype.updateButtonsVisibility = function() {

    if (this.currentTab === 0) {
        this.elements.btnPrev.classList.add("hidden");
    } else {
        this.elements.btnPrev.classList.remove("hidden");
    }

    if (this.currentTab === this.steps.length - 1) {
        this.elements.btnNext.classList.add("hidden");
        this.elements.btnFinish.classList.remove("hidden");
    } else {
        this.elements.btnNext.classList.remove("hidden");
        this.elements.btnFinish.classList.add("hidden");
    }
}

Tour.prototype.refreshTab = function(index) {
    this.popover.dispose();
    this.currentTab = index;
    this.show();



    var lis = this.popover.tip.getElementsByClassName("tour-tab-links")[0].getElementsByTagName("a");
    for (var i = 0; i < lis.length; i++) {
        if (i === index) {
            lis[i].classList.add("active");
        } else {
            lis[i].classList.remove("active");
        }

    }

    var tabs = this.popover.tip.getElementsByClassName("tour-tab");
    for (var j = 0; j < tabs.length; j++) {
        if (j === index) {
            tabs[j].classList.add("active");
        } else {
            tabs[j].classList.remove("active");
        }

    }
}