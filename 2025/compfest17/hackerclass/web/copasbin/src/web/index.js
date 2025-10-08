const express = require('express');
const app = express();
const fs = require('fs');
const path = require('path');
const { sanitize } = require('express-xss-sanitizer');
const _ = require('lodash');
const axios = require('axios');
const port = process.env.PORT || 3000;

app.use(express.static(path.join(__dirname, 'public')));
app.use(express.urlencoded({ extended: false }));
app.use(express.json());
app.set('view engine', 'ejs');

function SanitizerObject(data, allowedTags, allowedKeys) {
    let object = Object.create(Object.create({}));

    if (data) {
        object.data = data;
    }

    // not sure if i want this :/
    // if (allowedTags) {
    //     object.allowedTags = allowedTags;
    // }
    //
    // if (allowedKeys) {
    //     object.allowedKeys = allowedKeys;
    // }

    return object;
}

app.get('/', (req, res) => {
    res.render('index');
});

app.get('/copas/:id', (req, res) => {
    let filepath = path.join(__dirname, path.normalize('uploads/' + req.params.id));
    if (filepath.indexOf(path.join(__dirname, 'uploads/')) !== 0) {
        res.status(403).render('errors/403');
        return
    }

    try {
        fs.readFileSync(filepath);
        res.render('copas', { 'filename': req.params.id, 'data': fs.readFileSync(filepath) });
    } catch (e) {
        res.status(404).render('errors/404');
    }
});

app.get('/api/copas/:id', (req, res) => {
    let filepath = path.join(__dirname, path.normalize('uploads/' + req.params.id));
    if (filepath.indexOf(path.join(__dirname, 'uploads/')) !== 0) {
        res.status(403).json({ 'status': 'error' });
        return
    }

    try {
        res.json({ 'status': 'success', 'filename': req.params.id, 'data': fs.readFileSync(filepath).toString() });
    } catch (e) {
        res.status(404).json({ 'status': 'error', 'data': '' });
    }
});

app.post('/api/copas', (req, res) => {
    req.body['data'] = req.body['data'].toLowerCase();

    let sanitizeObject = _.merge(SanitizerObject([], ['h1', 'h2', 'h3']), req.body);
    let sanitized = sanitize(sanitizeObject, sanitizeObject)['data'];

    let filename = require('crypto').createHash('sha256')
        .update((new Date()).valueOf().toString() + Math.random().toString())
        .digest('hex');

    if (!fs.existsSync('uploads/')) {
        fs.mkdirSync('uploads/');
    }

    try {
        fs.writeFileSync('uploads/' + filename, sanitized, (err) => {
            if (err) {
                res.status(500).json({ 'status': 'error' });
            }
        });
    } catch (e) {
        res.status(500).json({ 'status': 'error' });
    }

    res.json({ 'status': 'success', 'id': filename, 'data': sanitized });
});

app.put('/api/copas/:id', (req, res) => {
    req.body['data'] = req.body['data'].toLowerCase();

    let sanitizeObject = _.merge(SanitizerObject([], ['h1', 'h2', 'h3']), req.body);
    let sanitized = sanitize(sanitizeObject, sanitizeObject)['data'];

    let filepath = path.join(__dirname, path.normalize('uploads/' + req.params.id));
    if (filepath.indexOf(path.join(__dirname, 'uploads/')) !== 0) {
        res.status(403).json({ 'status': 'error' });
        return
    }

    try {
        if (!fs.existsSync(filepath)) {
            res.status(404).json({ 'status': 'error' });
            return
        }

        fs.writeFileSync(filepath, sanitized, (err) => {
            if (err) {
                res.status(500).json({ 'status': 'error' });
            }
        });
    } catch (e) {
        res.status(500).json({ 'status': 'error' });
        return
    }

    res.json({ 'status': 'success', 'id': req.params.id, 'data': sanitized });
});

app.post('/api/copas/report/:id', (req, res) => {
    try {
        axios.post('http://copasbin-bot:9999/visit', {
            'id': req.params.id,
        }).then(() => {
            res.json({ 'status': 'success', 'id': req.params.id });
        })
    } catch (e) {
        res.status(500).json({ 'status': 'error' });
        return
    }
});

app.listen(port, () => {
    console.log(`Example app listening on port ${port}!`);
});
