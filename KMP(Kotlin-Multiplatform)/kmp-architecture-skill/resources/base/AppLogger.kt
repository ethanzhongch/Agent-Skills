package com.lite.skill.base

import io.github.aakira.napier.Napier
import io.github.aakira.napier.DebugAntilog

/**
 * AppLogger abstraction to decouple the project from specific logging libraries (DIP).
 * Focused on local debugging needs.
 */
object AppLogger {
    
    fun init() {
        // Initialize Napier with DebugAntilog for local development.
        Napier.base(DebugAntilog())
    }

    /** Verbose */
    fun v(message: String, tag: String? = null) {
        Napier.v(message, tag = tag)
    }

    /** Debug */
    fun d(message: String, tag: String? = null) {
        Napier.d(message, tag = tag)
    }

    /** Info */
    fun i(message: String, tag: String? = null) {
        Napier.i(message, tag = tag)
    }

    /** Warning */
    fun w(message: String, throwable: Throwable? = null, tag: String? = null) {
        Napier.w(message, throwable, tag)
    }

    /** Error */
    fun e(message: String, throwable: Throwable? = null, tag: String? = null) {
        Napier.e(message, throwable, tag)
    }
}
